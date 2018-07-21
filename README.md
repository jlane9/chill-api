Run:

```bash
virtualenv venv3 -p python3
source venv3/bin/activate
pip install -r requirements.txt
```


Routes:

POST /api/createSession

```json
{
    "username": "<str>"
    "token": "<str>"
}
```