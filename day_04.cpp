#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cinttypes>

#include <thread>
#include <mutex>
#include <algorithm>
#include <vector>

#include <openssl/md5.h>

static_assert(__BYTE_ORDER == __LITTLE_ENDIAN, "ah!");

struct Distrib {
    std::mutex m_mutex;
    uint64_t m_next;
    bool m_done;
    uint64_t m_result;

    Distrib() : m_mutex(), m_next(0), m_done(false), m_result(-1) {}

    bool get_next_chunk(uint64_t &next, uint64_t &len) {
        std::lock_guard<std::mutex> lock(m_mutex);
        if (m_done) {
            return false;
        }
        next = m_next;
        len = (1<<20);
        m_next += len;
        return true;
    }

    void set_result(uint64_t v) {
        std::lock_guard<std::mutex> lock(m_mutex);
        m_result = std::min(m_result, v);
        m_done = true;
    }

    void reset() {
        m_done = false;
        m_result = -1;
        m_next = 0;
    }
};

static Distrib distrib;

static void worker(const std::string &seed, uint32_t mask_part) {
    uint8_t buffer[128];
    uint32_t hash[4];
    uint64_t next, len;
    size_t offset = seed.size();
    ::memcpy(buffer, seed.data(), seed.size());

    while (distrib.get_next_chunk(next, len)) {
        for (uint64_t n = next; n < next + len; ++n) {
            size_t r = sprintf(reinterpret_cast<char *>(buffer) + offset, "%" PRIu64, n);
            MD5(buffer, offset + r, reinterpret_cast<uint8_t *>(hash));
            if ((hash[0] & mask_part) == 0) {
                distrib.set_result(n);
                return;
            }
        }
    }
}

int main() {
    const std::string input = "iwrupvqb";

    std::vector<std::thread> threads;
    for (unsigned int n = 0; n < std::thread::hardware_concurrency(); ++n) {
        threads.emplace_back(worker, input, 0xF0FFFF);
    }
    for (auto &th : threads) {
        th.join();
    }

    printf("part 1: %" PRIu64 "\n", distrib.m_result);

    distrib.reset();
    threads.clear();
    for (unsigned int n = 0; n < std::thread::hardware_concurrency(); ++n) {
        threads.emplace_back(worker, input, 0xFFFFFF);
    }
    for (auto &th : threads) {
        th.join();
    }

    printf("part 2: %" PRIu64 "\n", distrib.m_result);
    
    return 0;
}
