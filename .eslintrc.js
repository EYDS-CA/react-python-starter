module.exports = {
  parser: "babel-eslint",
  root: true,
  env: {
    node: true,
    browser: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "airbnb-base",
    "prettier",
    "prettier/react",
  ],
  parserOptions: {},
  settings: {
    react: {
      version: "detect",
    },
  },
};
