import easyDB from 'easydb-io'
      
const db = easyDB({
  database: '993b07f5-1830-4c98-871f-66b34ad3c9c8',
  token: 'abaac270-e1d2-4bcd-867d-1dab05f0986c'
})
      
// Use a callback
db.put('myKey', {some: 'data'}, err => console.log(err))
db.get('myKey', (err, value) => console.log(value, err))
db.delete('myKey', err => console.log(err))
db.list((err, value) => console.log(value, err))
   
// Or, async/await
(async() => {
  let value, values
  value = await db.put('myKey', {some: 'data'}) 
  value = await db.get('myKey')
  value = await db.delete('myKey')
  values = await db.list()
  console.log(values);
})()
