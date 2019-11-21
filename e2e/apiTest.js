const {success, fail} = require('./helpers');

// Tests that the API is successfully integrated with the UI
module.exports = async browser => {
  const errors = [];
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/about-us');
  const responseDataElement = await page.$('p');

  try {
    const responseData = await page.evaluate(
      element => element.textContent,
      responseDataElement,
    );
    // TODO: Update to reference seed data
    const expected = 'no response data';
    const actual = responseData.toLowerCase();
    if (actual.includes(expected)) {
      success();
    } else {
      fail();
      errors.push(
        `Response data expected to include "${expected}" but was: "${actual}"`,
      );
    }
  } catch (e) {
    errors.push(e);
  }

  return errors;
};
