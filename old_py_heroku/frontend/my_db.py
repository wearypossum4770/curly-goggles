import easydbio

db = easydbio.DB({
  "database": "993b07f5-1830-4c98-871f-66b34ad3c9c8",
  "token": "abaac270-e1d2-4bcd-867d-1dab05f0986c"
})

db.Put("key", "8")
print(db.Get("key"))
print(db.List())
