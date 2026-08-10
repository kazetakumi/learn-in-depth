# Source inventory

Everything the ladder is grounded in. No claim in any lesson should lack a home here.

## Videos

| Source | Length | Shape |
|---|---|---|
| Dr. Chuck — *Learn C Programming and OOP* (`PaPN51Mm5qQ`) | 18h35m | K&R ch1–6 read line by line, then an original OOP-in-C module rebuilding Python's str/list/dict, then an epilogue on CPython internals with a Guido van Rossum interview |
| Caleb Curry — *C Programming All-in-One* (`Bz4MxDeEM6k`) | 10h12m | Beginner course: toolchain → types → operators → logic → loops → arrays → strings → functions → pointers → structs. Stops at structs. No captions on YouTube; transcribed locally with mlx-whisper large-v3-turbo |

**Both videos stop short of:** file I/O, the system-call boundary, linking, libraries, error-handling design, concurrency, security, and build systems.

## Books

| Book | Role |
|---|---|
| **K&R, *The C Programming Language* 2e** | The canon. Ch7 (stdio) and ch8 (UNIX interface) are the gap both videos leave. Ch8 has you *implement* `fopen`, `getc` and `malloc` |
| **K.N. King, *C Programming: A Modern Approach* 2e** | The complete modern reference — 27 chapters. Only source covering `<stdint.h>`, type qualifiers, C99, and **ch19 Program Design** (modules, information hiding, ADTs) |
| **Zed Shaw, *Learn C the Hard Way*** | Practice and discipline. Debugger at Exercise 4, Makefiles at Exercise 2. The C error-handling problem, `dbg.h`, the eight defensive-programming strategies, unit testing, real projects |
| ***Head First C*** | Systems half: small composable tools, static/dynamic libraries, `fork`/`exec`, pipes, signals, sockets, pthreads. Plus valgrind |
| **C Programming Absolute Beginner** | Thin; 37 pages. Marginal |

## Courses

| Course | What it contributes |
|---|---|
| **Stanford CS107 — Programming Paradigms** (27 video transcripts, 23 notes, 30 assignments) | The memory model taught with diagrams; generic containers via `void *` + element size + function pointer (the `Vector` assignment); function call and return *at the assembly level*; then how other languages are built on the same machine |
| **MIT 6.087 — Practical Programming in C** (14 notes, 20 psets) | Sequencing authority. File I/O at lecture 4. **Virtual memory** at lecture 5. Designing `malloc()` at lecture 11. Threads, mutexes, semaphores, signals, fork, pipes at 12–14 |
| **MIT 6.088 — C Memory Management** (9 notes) | "The C memory machine", data structures, GCC internals |
| **MIT 6.S096 — Effective Programming in C** (17 notes, 16 psets) | Assembly; **secure programming / stack smashing**; floating-point subtleties; design patterns; unit testing and code review; Makefiles for large projects |

## Topics found only in the deeper sources

Things no video teaches, surfaced by reading the books and course notes in full. These drove the ladder's growth.

- **`<stdint.h>` fixed-width types** (`int32_t`, `uint8_t`) — King ch27. Absent from K&R entirely; mandatory in modern portable C
- **Type qualifiers** — `const`, `volatile`, `restrict` — King 18.3, 17.8. These are API contracts, not decorations
- **Virtual memory and the process address space** — MIT 6.087 L5. Text/data/bss/heap/stack, and why every process sees its own addresses
- **Generic containers via `void *`** — CS107 `Vector`, MIT 6.087 L8. What `qsort` actually is
- **Opaque pointers / information hiding** — King 19.2–19.5. `struct Foo;` in the header, definition hidden in the `.c`. The central architectural move in C
- **The C error-handling problem** — LCTHW ex19/27. No exceptions, so failure must be encoded, checked, and cleaned up. `dbg.h`, `goto cleanup`, `setjmp`/`longjmp`
- **Static vs dynamic libraries** — `ar`, `.a`, `.so`/`.dylib`, `dlopen` — HFC ch8, MIT 6.087 L9
- **Buffer overflows and stack smashing** — MIT 6.S096 L3S. C's missing bounds check as an attack surface
- **IEEE 754 floating point** — MIT 6.S096 L2, King 23.1. Why `0.1 + 0.2 != 0.3`
- **Reading generated assembly** — MIT 6.S096 L3A, CS107. Two courses independently insist on it
- **Flexible array members** — King 17.9. The struct-with-trailing-array idiom, everywhere in real C
- **Varargs** — K&R 7.3, King 26.1. How `printf` itself is written
- **Wide characters and Unicode** — King ch25
- **Small composable tools** — HFC ch3. stdin/stdout/stderr, redirection, pipes as a *design* discipline
- **valgrind and sanitizers** — HFC ch6, LCTHW. Instruments for an invisible subject
- **Build systems and project layout** — Makefiles, unit tests, install targets — LCTHW ex2/28/30, MIT 6.S096 L9
- **Implement what you use**: `malloc` (K&R 8.7, MIT 6.087 L11), `fopen`/`getc` (K&R 8.5), `printf` (varargs)
