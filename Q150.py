def logging(lines):
    filtered=[]
    processed=0
    failed=0
    for line in lines:
        processed+=1
        try:
          if "ERROR" in   line or "WARN" in line or "Warning"  in  line :
            filtered.append()
        except:
           failed+=1
        summary={"processed": processed,"failed":failed}
log=["INFO ok","ERROR timeout","WARN disk low"]
print(logging(log))              