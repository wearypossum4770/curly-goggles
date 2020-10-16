const puppeteer = require('puppeteer');
//~ ssh_regex = /.*(last-used-at).*\s+.*\s+.*(datetime)\W+([0-9]{4}-[0-9]{2}-\w+=\w+=\w+).*\"(\w+\s+\w+,\s+\w+\s+\w+\W+\w+\s+\w+).*\s+.*\s+.*(expires)\s+.*\s+.*\s+(\w+)\s+.*\s+.*(key-created-at).*\s+.*(datetime)\W+([0-9]+-[0-9]+-\w+\W+\w+\W+\w+).*.*\"(\w+\s+\w+,\s+\w+\s+\w+\W+\w+\s+\w+).*\s+.*/gmi



const scrapper = async () => {
	
    try {
        const browser = await puppeteer.launch({
            headless: false
        });

        const page = await browser.newPage();
        await page.goto('https://gitlab.com/users/sign_in');
        
        await page.waitForNavigation({waitUntil: 'domcontentloaded'})
        
        await page.focus('input#user_login')
        await page.keyboard.type('wearypossum4770')
        await page.focus('input#user_password')
        await page.keyboard.type("K2DNQyfx9SRLU!b")
        await page.click("input[type='submit']")
        
        await page.waitForNavigation({waitUntil: 'domcontentloaded'})
        

        await page.goto("https://gitlab.com/profile/keys")
const ssh_regex = /.*\s+.*\s+.*(?<key_last_used>([0-9]{4}-[0-9]{2}-\w+=\w+=\w+)).*(?<humanize_last_used>([a-z]{3,}\s+\w+,\s+\w+\s+\w+=\w+\s+\w+)).*\s+.*\s+.*\s+.*\W+\s+.*\s+(?<key_expires>(\w+))\s+.*\s+.*\s+.*\"(?<date_key_created>(\w+-\w+-\w+=\w+=\w+\w+)).*\"(?<humanize_date_created>(\w+\s+\w+,\s+\w+\s+\w+=\w+\s+\w+)).*\s+.*\"(?<profile_href>(\/\w+\/\w+\/\w+)).*/gmi

        await page.screenshot({
			
            path: 'gitlab_screenshoot.png'
        });
        await browser.close();




    } catch (error) {
        console.log(error)
    }
}


console.log(scrapper())
//~ [class="d-flex align-items-center key-list-item"]
