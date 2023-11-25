{
    "devCommand":"uvicorn app:app --host 0.0.0.0 --port 5000"
    "builds":[
        {
            "src":"/api/app.py",
            "use":"@vercel/python"
        }
    ],
    "routes":[
           "src":"/(.*)",
           "use":"/api/app.py"
    ]
}