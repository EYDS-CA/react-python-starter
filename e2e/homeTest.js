const {success, fail} = require('./helpers');

// Tests that the / route loads successfully
module.exports = async browser => {
  const errors = [];
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/');
  const header = await page.$('h1');

  try {
    const headerText = await page.evaluate(
      element => element.textContent,
      header,
    );
    if (headerText.length > 0) {
      success();
    } else {
      fail();
      errors.push('Header not found');
    }
  } catch (e) {
    errors.push(e);
  }

  return errors;
};
