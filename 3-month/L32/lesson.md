# L32 — Practice: Advanced Topics

## Project brief
You are building a **concurrent web scraper and data processor** — a system that fetches data from multiple mock API endpoints concurrently, processes the results through a generator pipeline, manages resources with context managers, and caches expensive computations. This project ties together every Month 3 advanced topic: concurrency, context managers, metaclasses, and performance optimization.

---

## Requirements

1. Use `asyncio` to fetch data from 10 mock API endpoints concurrently
2. Implement a `RateLimiter` context manager that ensures no more than N requests per second
3. Use a `PluginMeta` metaclass to register data processors (JSON, CSV, filter)
4. Build a generator pipeline to process fetched records lazily
5. Apply `@lru_cache` to cache expensive transformation operations
6. Use `__slots__` for the high-volume `Record` data class
7. Profile the full pipeline with `cProfile` and show a before/after optimization comparison
8. Save processed results to a file; track peak memory with `tracemalloc`

---

## Milestones

**Milestone 1 (0:00–0:30) — Async data fetcher**
- Write `async def fetch_endpoint(name, delay)` simulating API calls
- Implement `RateLimiter` context manager
- Fetch all 10 endpoints concurrently with `asyncio.gather()`
- Verify rate limiting is respected

**Milestone 2 (0:30–1:00) — Plugin processor system**
- Write `ProcessorMeta` metaclass with auto-registry
- Implement `BaseProcessor(ABC)` + `JSONProcessor`, `CSVProcessor`, `FilterProcessor`
- Wire processors into a processing chain

**Milestone 3 (1:00–1:30) — Generator pipeline & caching**
- Build the full generator pipeline: parse → validate → transform → format
- Apply `@lru_cache` to the expensive transformation step
- Add `__slots__` to the `Record` class
- Measure memory with `tracemalloc`

**Milestone 4 (1:30–2:00) — Profiling & polish**
- Profile the entire pipeline with `cProfile`
- Identify the top 3 slowest functions
- Optimize at least one bottleneck and show the improvement
- Write final output to `results.json`

---

## Bonus challenges

1. **Thread-safe result accumulator:** Use `threading.Lock` to safely accumulate results from multiple async tasks into a shared list.
2. **Adaptive rate limiter:** Make the `RateLimiter` dynamically adjust its rate based on error responses (back off on 429, speed up on 200).
3. **Benchmark report:** Generate a `benchmark_report.txt` showing memory before/after `__slots__`, cache hit rate, and total pipeline time.

