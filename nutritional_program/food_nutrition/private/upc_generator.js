import puppeteer from 'puppeteer'

const url = 'https://barcode.tec-it.com/en/UPCA'
('data[value="EAN13CCA"]')

const url2 = 'https://barcode.tec-it.com/en/UPCA?data=72527273070'
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);
  



  await browser.close();
})();