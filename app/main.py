from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Importando as rotas
from app.routes import home, simulador, consulta, api

app = FastAPI()

# ===== CONFIGURAÇÃO DE ARQUIVOS ESTÁTICOS =====
STATIC_DIR = None
possible_paths = [
    "static",
    os.path.join(os.path.dirname(__file__), "static"),
    os.path.join(os.path.dirname(__file__), "..", "static"),
    "/var/task/static"
]

for path in possible_paths:
    if os.path.exists(path) and os.path.isdir(path):
        STATIC_DIR = path
        print(f"✅ Pasta static encontrada em: {STATIC_DIR}")
        break

if STATIC_DIR:
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
    print(f"📁 Static montado em: {STATIC_DIR}")
else:
    print("⚠️ Pasta static NÃO encontrada! Usando fallback.")

# ===== ROTAS =====
app.include_router(home.router)
app.include_router(simulador.router)
app.include_router(consulta.router)
app.include_router(api.router)

# ===== ROTAS DIRETAS PARA PWA =====
@app.get("/manifest.json")
async def get_manifest():
    from fastapi.responses import FileResponse
    manifest_path = None
    possible_paths = [
        "static/manifest.json",
        os.path.join(os.path.dirname(__file__), "static", "manifest.json"),
        os.path.join(os.path.dirname(__file__), "..", "static", "manifest.json")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            manifest_path = path
            break
    if manifest_path:
        return FileResponse(manifest_path, media_type="application/json")
    return {"error": "Manifest not found"}

@app.get("/sw.js")
async def get_sw():
    from fastapi.responses import FileResponse
    sw_path = None
    possible_paths = [
        "static/sw.js",
        os.path.join(os.path.dirname(__file__), "static", "sw.js"),
        os.path.join(os.path.dirname(__file__), "..", "static", "sw.js")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            sw_path = path
            break
    if sw_path:
        return FileResponse(sw_path, media_type="application/javascript")
    return {"error": "SW not found"}

@app.get("/logo")
async def get_logo():
    from fastapi.responses import FileResponse
    logo_path = None
    possible_paths = [
        "static/img/logo-jadlog.png",
        os.path.join(os.path.dirname(__file__), "static", "img", "logo-jadlog.png"),
        os.path.join(os.path.dirname(__file__), "..", "static", "img", "logo-jadlog.png")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            logo_path = path
            break
    if logo_path:
        return FileResponse(logo_path, media_type="image/png")
    return {"error": "Logo not found"}

@app.get("/icons/{icon_name}")
async def get_icon_root(icon_name: str):
    from fastapi.responses import FileResponse
    allowed_icons = [
        "launchericon-72x72.png", "launchericon-96x96.png", "launchericon-128x128.png",
        "launchericon-144x144.png", "launchericon-152x152.png", "launchericon-192x192.png",
        "launchericon-384x384.png", "launchericon-512x512.png"
    ]
    if icon_name not in allowed_icons:
        return {"error": "Icon not found"}
    
    possible_paths = [
        f"icons/{icon_name}",
        os.path.join(os.path.dirname(__file__), "icons", icon_name),
        os.path.join(os.path.dirname(__file__), "..", "icons", icon_name),
        f"static/icons/{icon_name}",
        os.path.join(os.path.dirname(__file__), "static", "icons", icon_name)
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return FileResponse(path, media_type="image/png")
    return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)