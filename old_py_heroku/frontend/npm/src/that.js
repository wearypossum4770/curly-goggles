const puppeteer = require('puppeteer');
//~ ssh_regex = /.*(last-used-at).*\s+.*\s+.*(datetime)\W+([0-9]{4}-[0-9]{2}-\w+:\w+:\w+).*\"(\w+\s+\w+,\s+\w+\s+\w+\W+\w+\s+\w+).*\s+.*\s+.*(expires)\s+.*\s+.*\s+(\w+)\s+.*\s+.*(key-created-at).*\s+.*(datetime)\W+([0-9]+-[0-9]+-\w+\W+\w+\W+\w+).*.*\"(\w+\s+\w+,\s+\w+\s+\w+\W+\w+\s+\w+).*\s+.*/gmi

console.save = function (data, filename) {
    if (!data) {
        console.error('Console.save: No data')
        return;
    }

    if (!filename) filename = 'story.json'

    if (typeof data === "object") {
        data = JSON.stringify(data, undefined, 4)
    }

    
    var blob = new Blob([data], {
            type: 'text/json'
        }),
        e = document.createEvent('MouseEvents'),
        a = document.createElement('a')

    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}



const scrapper = async () => {
    const ssh_array = []

    try {
        const browser = await puppeteer.launch({
            headless: false
        });

        const page = await browser.newPage();
        await page.goto('https://gitlab.com/users/sign_in');
        await page.waitForNavigation({
            waitUntil: 'domcontentloaded',
        })
        await page.focus('input#user_login')
        await page.keyboard.type('wearypossum4770')
        await page.focus('input#user_password')
        await page.keyboard.type("K2DNQyfx9SRLU!b")
        await page.click("input[type='submit']")
        await page.waitForNavigation({
            waitUntil: 'domcontentloaded',
        })
        await page.goto("https://gitlab.com/profile/keys")
        const ssh_array = []
        await page.$$eval(
            'li[class="d-flex align-items-center key-list-item"]',
            unordered_list => unordered_list.forEach(element => {
			const ssh_regex = /.*\s+.*\s+.*(?<key_last_used>([0-9]{4}-[0-9]{2}-\w+:\w+:\w+)).*(?<humanize_last_used>([a-z]{3,}\s+\w+,\s+\w+\s+\w+:\w+\s+\w+)).*\s+.*\s+.*\s+.*\W+\s+.*\s+(?<key_expires>(\w+))\s+.*\s+.*\s+.*\"(?<date_key_created>(\w+-\w+-\w+:\w+:\w+\w+)).*\"(?<humanize_date_created>(\w+\s+\w+,\s+\w+\s+\w+:\w+\s+\w+)).*\s+.*\"(?<profile_href>(\/\w+\/\w+\/\w+)).*/gmi

                const groups = element.match(ssh_regex).groups
                const ssh_obj = {}
                ssh_array.push(
                    Object.defineProperties(ssh_obj, {
                            profile_href: {
                                value: groups.profile_href,
                                writeable: true,
                            },
                            key_last_used: {
                                value: groups.key_last_used,
                                writeable: true,
                            },
                            humanize_last_used: {
                                value: groups.humanize_last_used,
                                writeable: true,
                            },
                            date_key_created: {
                                value: groups.date_key_created,
                                writeable: true,
                            },
                            humanize_date_created: {
                                value: groups.humanize_date_created,
                                writeable: true,
                            },
                            key_expires: {
                                value: groups.key_expires,
                                writeable: true,
                            }


                        }

                    )
                )

            }))

        await page.screenshot({
            path: 'gitlab_screenshoot.png'
        });
        await browser.close();




    } catch (error) {
        console.log(error)
    }
}


console.log(scrapper())
