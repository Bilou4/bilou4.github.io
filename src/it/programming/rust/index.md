# Rust

## Things to know

- no variadic functions (unknown number of parameters), except for macros `println!(...)`.
- `dbg!()` allows to debug an expression and also returns the result
  - ```rust
    let a = dbg!(5+1)+8;
    println!("{a}");
    ```

## Good practice

- [rust-api guidelines](https://rust-lang.github.io/api-guidelines/about.html)

## Build

By default, binaries are compiled in `unwind` mode which raises the call stack. Using `abort` allows to have smaller binaries but the `Drop` is not done (memory not cleared).

```toml
[profile.release]
panic = 'abort'
```

Performing a `panic` in a `panic` is equivalent to an `abort`, it is a bad practice.

## Linters

- [Clippy](https://github.com/rust-lang/rust-clippy): A collection of lints to catch common mistakes and improve your Rust code.
- [miri](https://github.com/rust-lang/miri): An interpreter for Rust's mid-level intermediate representation.
- [valgrind](https://valgrind.org/): detect many memory management and threading bugs, and profile your programs in detail.
- [cargo-geiger](https://github.com/rust-secure-code/cargo-geiger): Detects usage of unsafe Rust in a Rust crate and its dependencies.

