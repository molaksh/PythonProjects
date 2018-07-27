




for ctemp in container
    link = ctemp.a["href"]
    name = ctemp.a.img["alt"]
    
    
    for c in ctemp
        c = cont.findAll("div",{"class":"a-section a-spacing-micro"})
        author = c.