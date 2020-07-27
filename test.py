from notion.client import NotionClient
import notion
import os
client = NotionClient(token_v2="3aed2d24ae9d2941e182b56d953c71827237e869c6d279d7d5478e12e658794182ce4dcfbd5b232b19c5a72623b1046050f9c71e1f31d352141b31787af154a90658eeadac23dd1583b216188568")
cv = client.get_collection_view('https://www.notion.so/jerrywang959/2817126c1e1249ee940ea26926ca2a18?v=53f80755f5ca45108502b65b7e583842')
pagelist=cv.collection.get_rows()
x=pagelist[5]