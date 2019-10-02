# React Frontend

## Getting Started

Start a local development build of the project

```
$ npm start
```

## Development

### Linting and Formatting

This project has been pre-configured with Prettier and ESLint to work with the
provided tooling/environments. A typical IDE will observe the configuration
files automatically.

If you run into difficulties with IDE-based formatting, you can use the
provided npm script to apply formatting to the codebase.

```
$ npm run format
```

A similar script exists for linting

```
$ npm run lint
```

#### IDE Configuration for Formatting

This codebase uses Prettier for formatting. This means that the IDE being used
should have any other formatters (ex. Beautify) disabled. If the IDE provides
formatting on-save, it is beneficial to enable that setting.

If your IDE is not observing the configuration file(s) correctly, it is
advisable to disable all auto-formatting to avoid inconsistencies.
