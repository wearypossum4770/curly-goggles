from  asyncio import get_event_loop
import asyncpg
import datetime


async def main():
	conn = await asyncpg.connect('postgresql://postgres@localhost/gardening')
	await conn.execute('''CREATE TABLE florida_hill_nursery()''')

	
	await conn.close()

get_event_loop().run_until_complete(main())



florida_hill_nursery (
id serial primary key,
unique_id uuid not null,
is_in_stock 
product_name 
image_urls
images_url
product_description
)
