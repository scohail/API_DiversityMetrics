import { app, BrowserWindow, ipcMain } from "electron";
import registerListeners from "./helpers/ipc/listeners-register";
// "electron-squirrel-startup" seems broken when packaging with vite
//import started from "electron-squirrel-startup";
import path from "path";

import { PythonShell } from 'python-shell';



const inDevelopment = process.env.NODE_ENV === "development";

function createWindow() {
    const preload = path.join(__dirname, "preload.js");
    const mainWindow = new BrowserWindow({
        width: 900,
        height: 600,
        minWidth: 900,
        webPreferences: {
            devTools: inDevelopment,
            contextIsolation: true,
            nodeIntegration: true,
            nodeIntegrationInSubFrames: false,

            preload: preload,
        },
        titleBarStyle: "hidden",
    });
    registerListeners(mainWindow);

    if (MAIN_WINDOW_VITE_DEV_SERVER_URL) {
        mainWindow.loadURL(MAIN_WINDOW_VITE_DEV_SERVER_URL);
    } else {
        mainWindow.loadFile(
            path.join(__dirname, `../renderer/${MAIN_WINDOW_VITE_NAME}/index.html`)
        );
    }
    mainWindow.webContents.openDevTools();
}

app.whenReady().then(createWindow);

//osX only
app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});

app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
//osX only ends



// Handle IPC messages from renderer process
ipcMain.handle('run-python-script', async (event,scriptPath, jsonContent) => {
    console.log('Received run-python-script IPC message:', scriptPath, jsonContent);

    if (!jsonContent) {
        throw new Error('jsonContent is required');
    }
    
    const options = { args: [jsonContent] }; 
    console.log('Running Python script with options:', options);
    try {
        const results = await PythonShell.run(scriptPath, options);
        console.log('Python script output:', results);
        return results;
    } catch (err) {
        console.error('Error running Python script:', err);
        throw err; // Send error back to renderer process
    }
});
