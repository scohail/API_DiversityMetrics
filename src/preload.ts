import exposeContexts from "./helpers/ipc/context-exposer";
import { ipcRenderer, contextBridge } from "electron";

exposeContexts();

contextBridge.exposeInMainWorld('electron', {
    runPythonScript: (scriptPath: string 
         ,jsonContent: Record<string, any>) =>
        ipcRenderer.invoke('run-python-script',scriptPath, jsonContent)
});