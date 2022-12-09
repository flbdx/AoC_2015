CXXFLAGS=-Wall -Wextra
CXXFLAGS+=-O2 -g -std=c++17 -march=native

TARGETS=day_04 day_11

all: $(TARGETS)

day_04: LDLIBS=-lcrypto

clean:
	rm -f $(TARGETS)

.phony: all clean
