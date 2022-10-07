# Pre-Commit Hooks
Custom pre-commit hooks for [pre-commit](https://pre-commit.com/).


## Usage
Add the following to your `.pre-commit-config.yaml` file:

```yaml
-   repo: https://github.com/pythrick/pre-commit-hooks
    rev: v0.1.0
    hooks:
    -   id: check-changelog-updated
```

## Hooks available
- `check-changelog-updated`: Checks if the changelog has been updated.

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more information.

## Code of Conduct
This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
Please report unacceptable behavior to [patrick.pwall@gmail.com](mailto:patrick.pwall@gmail.com).

