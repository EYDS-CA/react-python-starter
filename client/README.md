# React Frontend

This codebase is a minimal React starter with the following features:

- BrowserRouter client-side routing
- Webpack with Babel for code transformation and bundling
- Jest (with snapshot) testing

And the following development tooling:

- ESLint
- Prettier formatting
- SASS support
- Webpack Dev Server with hot module replacement

## Getting Started

Start a local development build of the project

```
$ npm run serve
```

## Development

### Examples

The `index.html` file is used as a template for the built `index.html` that
will be created in `/dist`. If you need to add third-party scripts to your
build, you may choose to add them here. Note that the output bundle for your
build will be injected into the template. If you modify the template directly,
be careful not to create a conflict with the injected bundle.

Routing is controlled by a Switch component in `Routes.js`.

The following sample components are provided:

- Home: The landing-page component. It includes a Link to `/about-us` as an
  example of routing to another page/component. It also provides an example of
  conditional rendering based on incoming props. Sample Jest snapshot tests are
  provided for this component.
- AboutUs: A stateful component with an example API request integrated into the
  component state.
- NotFound: A stateless component used as the fall-through if no other routes
  are matched.

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
