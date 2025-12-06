service=[]
def handle(request):
    method, path=request.split()
    if method=="GET" and path=="/items":
        return service
    if method=="POST" and path =="/items":
        new_service={"id":101,"Endpoint":"pc-device"}
        service.append(new_service)
        return new_service
    if method=="GET" and path.startswith =="/items/":
        service_id=int(path.split("/")[-1])
        return service_id
    for s in service:
        s["id"]=service_id
        return s
    return "not found"
print(handle("POST /items"))
print(handle("GET /items"))
            
