workflow "Build and Publish" {
  on = "push"
  resolves = "Test"
}

action "Test" {
  uses = "actions/setup-node@v1"
  with = "10.x"
  runs = "npm ci"
  runs = "npm test"
}
