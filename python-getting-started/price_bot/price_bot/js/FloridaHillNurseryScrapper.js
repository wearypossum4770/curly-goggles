import request from "request";
import cheerio from "cheerio";
import fs from "fs";
const regex_expression = /http\w*\W+\w+\.\w+\/product\/(.*)\//;

const FloridaHillNurseryScrapper = (url) =>
  request(url, (error, response, html) => {
    console.log("Starting scrape of Florida Hill Nursery\n");
    if (!error && response.statusCode == 200) {
      console.log("Scrapping.........\n");
      const $ = cheerio.load(html);
      const meta_data = {
        url: url,
        product: {
          name: $(".entry-title").text(),
          unit_price: $("#prodpagemain .amount").text(),
          category: $(".posted_in").children('a[rel="tag"] ').text(),
          other_names: $("h3:nth-child(14)").text(),
          other_names_description: $("p:nth-child(15)").text(),
          keywords: $(".tagged_as")
            .text()
            .replace("Tags", "")
            .replace(":", "")
            .split(","),
        },
        description: {
          short: $(".woocommerce-product-details__short-description p").text(),
          long: $("h2+ p").text(),
        },
        vendor: {
          vendor_sku: $(".sku").text(),
          inventory: $(".out-of-stock").text(),
        },
        img: {
          primary: $(".wp-post-image").attr("src"),
          secondary: $(".wp-post-image").attr("srcset").split(","),
        },
        care_instructions: {
          light_and_water: $("p:nth-child(9),p:nth-child(8)").text().split("."),
          pest_and_diseases: $("p:nth-child(12)").text(),
          general_care: $("#tab-description li").text().split("."),
        },
      };
      console.log("Ending scrape of Florida Hill Nursery\n");
      console.log(meta_data);
      return meta_data;
    }
  });

export default FloridaHillNurseryScrapper;
