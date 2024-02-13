const puppeteer = require('puppeteer');

async function scrapeData() {
 const browser = await puppeteer.launch();
 const page = await browser.newPage();
 await page.goto('https://loja.imdepa.com.br/categoria/mancais');

 const data = await page.evaluate(() => {
    const elements = document.querySelectorAll('.y-item mt-none hidden-btn-reveal');
    return Array.from(elements).map(element => {
      return {
        name: element.querySelector('.product-name').innerText,
        price: element.querySelector('.product-price').innerText,
        // Add other attributes as needed
      };
    });
 });

 console.log(data);

 await browser.close();
}

scrapeData();