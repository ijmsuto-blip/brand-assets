import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
B="https://raw.githubusercontent.com/ijmsuto-blip/brand-assets/master/"
COLS=["Handle","Title","Body (HTML)","Vendor","Product Category","Type","Tags","Published","Option1 Name","Option1 Value","Option2 Name","Option2 Value","Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty","Variant Inventory Policy","Variant Fulfillment Service","Variant Price","Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Image Src","Image Position","Image Alt Text","Variant Image","SEO Title","SEO Description","Status"]
SIZES=["XS","S","M","L","XL","XXL"]
def rows(handle,title,body,vendor,ptype,tags,colours,price,compare,imgs,grams,seo,sizes=SIZES,cat="Apparel & Accessories > Clothing"):
    out=[];first=True
    for c in colours:
        for s in sizes:
            r={k:"" for k in COLS}
            r.update({"Handle":handle,"Option1 Name":"Colour","Option1 Value":c,"Option2 Name":"Size","Option2 Value":s,
              "Variant SKU":f"{handle}-{c[:3].lower()}-{s}","Variant Grams":grams,"Variant Inventory Tracker":"shopify","Variant Inventory Qty":"0",
              "Variant Inventory Policy":"continue","Variant Fulfillment Service":"manual","Variant Price":price,"Variant Compare At Price":compare,
              "Variant Requires Shipping":"TRUE","Variant Taxable":"TRUE","Variant Image":imgs.get(c,imgs["_"])})
            if first:
                r.update({"Title":title,"Body (HTML)":body,"Vendor":vendor,"Product Category":cat,"Type":ptype,"Tags":tags,"Published":"TRUE",
                  "Image Src":imgs["_"],"Image Position":"1","Image Alt Text":title,"SEO Title":seo[0],"SEO Description":seo[1],"Status":"active"})
                first=False
            out.append(r)
    pos=2
    for c,u in imgs.items():
        if c!="_" and u!=imgs["_"]:
            r={k:"" for k in COLS}; r.update({"Handle":handle,"Image Src":u,"Image Position":str(pos),"Image Alt Text":f"{title} in {c}"}); out.append(r); pos+=1
    return out

PRE='<p><strong>Drop 01 pre-order.</strong> Made in small runs and shipped from Hamilton, NZ in 3–4 weeks. Free NZ shipping over $150. 30-day returns.</p>'
L=B+"longwhite/"
lw=[
 ("heavyweight-hood","Heavyweight Hood — 400 GSM","<p>The one you reach for every day. Dense 400 GSM brushed-back cotton fleece, double-layer hood with no drawcords, ribbed cuffs that hold shape wash after wash.</p><ul><li>100% cotton fleece, 400 GSM</li><li>Relaxed fit, dropped shoulder</li><li>The bar chest print</li></ul>"+PRE,"Hoodies","hoodie, heavyweight, drop-01, preorder",["Ironsand","Fog","Tussock"],"159","",{"_":L+"p-hood-ironsand.jpg","Fog":L+"p-hood-fog.jpg","Tussock":L+"p-hood-tussock.jpg","Ironsand":L+"p-hood-ironsand.jpg"},"900"),
 ("full-zip-hood","Full-Zip Hood — 400 GSM","<p>Same heavyweight fleece as the Hood with a metal two-way zip. Layers over a tee, under a jacket.</p><ul><li>100% cotton fleece, 400 GSM</li><li>Relaxed fit, dropped shoulder</li></ul>"+PRE,"Hoodies","hoodie, heavyweight, drop-01, preorder",["Ironsand","Moss"],"179","",{"_":L+"p-zip.jpg"},"950"),
 ("boxy-crew","Boxy Crew — 400 GSM","<p>A cropped, boxy crewneck with a wide rib hem. Sits right with the Relaxed Sweatpant.</p><ul><li>100% cotton fleece, 400 GSM</li><li>Boxy, cropped 4 cm</li></ul>"+PRE,"Hoodies","crew, heavyweight, drop-01, preorder",["Fog","Bone","Ironsand"],"139","",{"_":L+"p-crew.jpg"},"800"),
 ("oversized-tee","Oversized Tee — 280 GSM","<p>Heavy jersey that drapes instead of clinging. Thick 3 cm neck rib that won’t bacon. Pre-shrunk.</p><ul><li>100% combed cotton jersey, 280 GSM</li><li>Oversized, dropped shoulder</li></ul>"+PRE,"Tees","tee, heavyweight, drop-01, preorder",["Ironsand","Bone","Moss"],"75","",{"_":L+"p-tee.jpg"},"350"),
 ("pocket-box-tee","Pocket Box Tee — 250 GSM","<p>Boxy fit with a chest pocket. Organic cotton, garment dyed for a lived-in colour.</p><ul><li>100% organic cotton jersey, 250 GSM</li><li>Boxy fit</li></ul>"+PRE,"Tees","tee, drop-01, preorder",["Bone","Fog"],"69","",{"_":L+"p-pocket-tee.jpg"},"320"),
 ("oversized-long-sleeve","Oversized Long Sleeve — 280 GSM","<p>The Oversized Tee with full-length sleeves and a long rib cuff to push up.</p><ul><li>100% combed cotton jersey, 280 GSM</li><li>Oversized</li></ul>"+PRE,"Tees","long-sleeve, drop-01, preorder",["Ironsand","Fog"],"85","",{"_":L+"p-ls.jpg"},"420"),
 ("tracksuit-set","Tracksuit Set — Hood + Sweatpant","<p>The Heavyweight Hood and the Relaxed Sweatpant in one matching colour. $278 bought separately. Choose your hoodie size; the sweatpant ships in the same size (swap free within 30 days).</p><ul><li>Hood 400 GSM + Sweatpant 350 GSM, 100% cotton fleece</li></ul>"+PRE,"Sets","set, heavyweight, drop-01, preorder",["Ironsand","Fog"],"249","278",{"_":L+"p-set.jpg"},"1700"),
 ("relaxed-sweatpant","Relaxed Sweatpant — 350 GSM","<p>Deep side pockets, back zip pocket for your phone, wide elastic waist with a flat drawcord.</p><ul><li>100% brushed-back cotton fleece, 350 GSM</li><li>Relaxed, tapered to cuff</li></ul>"+PRE,"Pants","sweatpant, heavyweight, drop-01, preorder",["Ironsand","Fog","Tussock"],"119","",{"_":L+"p-sweatpant.jpg"},"800"),
 ("straight-leg-trackpant","Straight Leg Trackpant — 350 GSM","<p>Open hem that stacks on sneakers. Same fleece as the Relaxed Sweatpant.</p><ul><li>100% brushed-back cotton fleece, 350 GSM</li><li>Straight, open hem</li></ul>"+PRE,"Pants","trackpant, heavyweight, drop-01, preorder",["Moss","Ironsand"],"125","",{"_":L+"p-trackpant.jpg"},"820"),
]
os.makedirs("csv",exist_ok=True)
with open("csv/longwhite-products.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=COLS); w.writeheader()
    for h,t,b,ty,tg,co,p,cp,im,g in lw:
        for r in rows(h,t,b,"LONGWHITE",ty,tg,co,p,cp,im,g,(t+" | LONGWHITE",f"{t}. Premium heavyweight basics, designed in Hamilton NZ. Free NZ shipping over $150.")): w.writerow(r)

R=B+"rewire/"
MTO='<p><strong>Made to order.</strong> Each piece is embroidered in New Zealand after you order and ships in 10–14 days. Free NZ shipping over $150. 30-day returns on unworn items.</p>'
def q(stitch,source,meaning): return f'<p><em>“{stitch}”</em> — {source}.</p><p>{meaning}</p>'
rw=[
 ("be-still-tee","Be still — Embroidered Tee",q("Be still","Psalm 46:10 (KJV)","Pause; you don’t have to carry everything. Stitched small on the left chest in charcoal thread on a bone-white 280 GSM heavyweight tee."),"Tees","tee, sacred, stillness, made-to-order",["Bone"],"79",{"_":R+"tee-bone-be-still.jpg"},"350"),
 ("know-thyself-tee","Know thyself — Embroidered Tee",q("Know thyself","Delphic maxim, Temple of Apollo","Self-knowledge is the first step. Stitched small on the left chest in bone thread on a washed-black 280 GSM heavyweight tee."),"Tees","tee, sage, growth, made-to-order",["Black"],"79",{"_":R+"tee-black-know-thyself.jpg"},"350"),
 ("if-not-now-when-tee","If not now, when? — Embroidered Tee",q("If not now, when?","Hillel, Pirkei Avot 1:14","Start now. Stitched small on the left chest in charcoal thread on a bone-white 280 GSM heavyweight tee."),"Tees","tee, sacred, growth, made-to-order",["Bone"],"79",{"_":R+"tee-bone-if-not-now-when.jpg"},"350"),
 ("kia-kaha-hood","Kia kaha — Embroidered Hood",q("Kia kaha","te reo Māori, ‘stay strong’","Stay strong. Stitched small on the left chest in bone thread on a black 400 GSM heavyweight hood."),"Hoodies","hoodie, warrior, strength, made-to-order",["Black"],"169",{"_":R+"hood-black-kia-kaha.jpg"},"900"),
 ("fear-not-hood","Fear not — Embroidered Hood",q("Fear not","Isaiah 41:10 (KJV)","You never face it alone. Stitched small on the left chest in charcoal thread on a bone-white 400 GSM heavyweight hood."),"Hoodies","hoodie, sacred, strength, made-to-order",["Bone"],"169",{"_":R+"hood-bone-fear-not.jpg"},"900"),
 ("master-of-myself-hood","Master of myself — Embroidered Hood",q("Master of myself","Epictetus, Fragments","Freedom starts with self-command. Stitched small on the left chest in bone thread on a black 400 GSM heavyweight hood."),"Hoodies","hoodie, sage, strength, made-to-order",["Black"],"169",{"_":R+"hood-black-master-of-myself.jpg"},"900"),
]
with open("csv/rewire-products.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=COLS); w.writeheader()
    for h,t,b,ty,tg,co,p,im,g in rw:
        for r in rows(h,t,b+MTO,"REWIRE",ty,tg,co,p,"",im,g,(t+" | REWIRE","Verified quotes, stitched small. Heavyweight basics embroidered in New Zealand."),sizes=["S","M","L","XL","XXL"]): w.writerow(r)
print("ok")
