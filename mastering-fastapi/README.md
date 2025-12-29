# Mastering FastAPI

## Installation
- There is a difference in installation of FastAPI and it all boils down to dependacy groups. Let's have a look at them. 

### 1. The baseline(no extras)
```
pip install fastapi
```

#### What you get
1. FastAPI itself
2. Pydantic(for validation)
3. Starlette(the ASGI framework)

#### What you do NOT get
1. An ASGI server(like uvicorn)
2. Common production/dev tooling(reload, websockets, etc.)

#### Use case
1. Almost never used alone
2. Only makes sense if you are managing all dependencies manually

### 2. ```fastapi[standard]``` --- the recommended default

```
pip install "fastapi[standard]"
```

#### What it installs(in addition to FastAPI itself)
1. uvicorn - ASGI server
2. uvicorn[standard] extras:

    - watchfiles - auto-reload in development
    - httptools - faster HTTP parsing
    - python-dotenv - ```.env``` file support

3. email-validator - for EmailStr
4. python-multipart - form/file uploads
5. jinja2 - templates(optional but common)

#### Why this exists
This is the "sane default" for:

    - Local development
    - Most production APIs
    - 90% of FastAPI projects

#### Use case
"I just want development server to work without thinking too much"

If you install only one version, this should be it.

### 3.```fastapi[all]``` --- everything and the kitchen sink

```
pip install "fastapi[all]"
```

#### What it does

    - Installs all optional features FastAPI can support:
    - GraphQL tools
    - ORMs integrations
    - Extra serializers
    - Additional utilities you may never use

#### Tradeoffs

    - Larger dependency tree
    - Slower installs
    - More security surface
    - Harder dependency management later

#### Use case

    - Learning/exploring FastAPI features
    - Tutorials
    - Prototyping where size does not matter

**Not recommended** for serious production work.

## Why the brackets exist ([...])

This is standard Python packaging syntax called extras.

Conceptually:
```
fastapi           → core framework
fastapi[standard] → core + common real-world tools
fastapi[all]      → core + everything optional
```

FastAPI itself is intentionally **minimal**. You opt into what you need.

## Making a Decision (use this every time)
First FastAPI project ---   fastapi[standard]
Production API ---	fastapi[standard]
Learning all features ---	fastapi[all]
Custom infra / Docker minimalism --- 	fastapi + manual deps

## Typical real-world setup (recommended)
```
python3 -m venv venv
source venv/bin/activate

pip install "fastapi[standard]"
```

Run:
```
uvicorn main:app --reload
```

This mirrors what you’d do with:

    - Django + django-admin

    - Vue + Vite

    - React + Next.js

A **batteries-included** starting point, not magic.

## Mental model (important)

FastAPI is not like Django.

    - Django → “install once, everything included”
    - FastAPI → “core + opt-in capabilities”

This design choice keeps FastAPI:

    - Fast
    - Modular
    - Cloud-native

8. Practical advice for you (based on your background)

You should default to:
```
pip install "fastapi[standard]"
```
And only add dependencies explicitly as your system grows (databases, auth, background jobs).
Given that probably you:

    - Are a full-stack developer
    - Use Django, Vue, HTMX
    - Care about production patterns