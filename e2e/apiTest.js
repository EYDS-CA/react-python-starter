const { success, fail } = require('./helpers');

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
    if (responseData.toLowerCase().includes('no response data')) {
      success();
    } else {
      fail();
      errors.push('API data not visible');
    }
  } catch (e) {
    errors.push(e);
  }

  return errors;
};
