class EmailData(BaseModel):
    recipient: str
    subject: str
    body: str
    scheduled_time: Optional[str] = None

@app.get("/")
async def read_root():
    return {"message": "Email Sender API"}

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    csv_data = []
    
    # Parse CSV content
    try:
        stream = io.StringIO(content.decode('utf-8'))
        csv_reader = csv.DictReader(stream)
        for row in csv_reader:
            csv_data.append(row)
        return {"data": csv_data, "columns": list(csv_data[0].keys()) if csv_data else []}
    except Exception as e:
        return {"error": str(e)}

@app.post("/schedule-emails/")
async def schedule_emails(emails: List[EmailData]):
    # This is a placeholder for email scheduling logic
    # In a real application, you'd add these to a task queue
    return {"scheduled": len(emails), "status": "pending"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)