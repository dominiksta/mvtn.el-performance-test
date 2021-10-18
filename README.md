# Performance Test for Mvtn.el

This repository contains note generator for
[mvtn.el](https://github.com/dominiksta/mvtn.el). It can be used to test the
performance of [mvtn.el](https://github.com/dominiksta/mvtn.el) with a very
large amount of notes.

# The Results

While I have not bothered measuring the exact performance, I can report that at
least on my system (nvme ssd + i7-1165G7), the performance is good even with
more than 800 notes per year (see `config/heavy_note_taker.py`). Listing notes
takes almost no time at all and the backlink buffer updates within ~0.5 seconds
even when using `grep` rather than `rg`. Performance only drops when setting
`mvtn-search-years` to a higher value than the default `3`.

# Running it Yourself

To run the performance tests, first install the dependencies (GNU make, Python
3, Emacs, Git). Then clone the repository with submodules:

```
git clone --recurse-submodules \
  https://github.com/dominiksta/mvtn.el-performance-test
```

After that, you can generate the test notes and launch a basic emacs
configuration with mvnt with the `run.py` script:

```
python3 run.py run --config <config>
```

`<config>` is the name of one of the files in `generator/config`. For example,
to see how mvtn performs for a rather heavy note taker, you can run

```
python3 run.py run --config heavy_note_taker
```