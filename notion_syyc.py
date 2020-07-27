from notion.client import NotionClient
import notion
import os
client = NotionClient(token_v2="3aed2d24ae9d2941e182b56d953c71827237e869c6d279d7d5478e12e658794182ce4dcfbd5b232b19c5a72623b1046050f9c71e1f31d352141b31787af154a90658eeadac23dd1583b216188568")
cv = client.get_collection_view('https://www.notion.so/jerrywang959/2817126c1e1249ee940ea26926ca2a18?v=53f80755f5ca45108502b65b7e583842')
pagelist=cv.collection.get_rows()

for idd in pagelist:
    x=client.get_block(idd.id)
    TTag="["+x.get_property("Tags")[0]
    if len(x.get_property("Tags"))==2:
        TTag=TTag+" ,"+x.get_property("Tags")[1]
    elif len(x.get_property("Tags"))==3:
        TTag=TTag+" ,"+x.get_property("Tags")[2]
    TTag=TTag+"]"

    content="---\ntitle: "+x.title+"\ndate: "+x.get_property("创建时间").strftime('%Y-%m-%d %H:%M:%S')+"\ntags: "\
        +TTag+"\npublished: true\nhideInList: "+x.get_property("是否隐藏")+"\nfeature: \nisTop: "\
            +x.get_property("是否置顶")+"\n---\n"

    for child in x.children:
        if isinstance(child,notion.block.TextBlock):
            content=content+"\n"+child.title
        elif isinstance(child,notion.block.NumberedListBlock):
            content=content+"\n"+"1. "+child.title
        elif isinstance(child,notion.block.HeaderBlock):  
            content=content+"\n"+"# "+child.title 
        elif isinstance(child,notion.block.SubheaderBlock):  
            content=content+"\n"+"## "+child.title 
        elif isinstance(child,notion.block.SubsubheaderBlock):  
            content=content+"\n"+"### "+child.title 
        elif isinstance(child,notion.block.CodeBlock):
            content=content+"\n```"+child.language+"\n"+child.title+"\n```"
        elif isinstance(child,notion.block.ImageBlock):
            content=content+"\n"+ "![]("+ child.source+ ")"
        elif isinstance(child,notion.block.CalloutBlock):
            content=content+"\n"+ "> "+ child.title

    filename="/home/jerrywang/Documents/Gridea/posts/"+x.title+".md"
    f = open(filename,'w')
    f.write(content)

    f.close()
