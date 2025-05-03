--- a/e:/OmniverseNet/QuantumDreamsAI/omnivision_channel.py
+++ b/e:/OmniverseNet/QuantumDreamsAI/omnivision_channel.py
@@ -1,11 +1,11 @@
 # Assuming module is renamed to cgx_api.py and class to CgxApi
-import cgx_api
+import CGX_API # Match the actual module filename if it's CGX_API.py
 import multiverse_streaming
 import parallel_universe_api

 # Initialize CGX API
-cgx_instance = cgx_api.CgxApi() # Using PascalCase for class, snake_case for variable
+cgx_instance = CGX_API.CGX_API() # Match the actual class name if it's CGX_API

 # Set up multiverse streaming
 streaming = multiverse_streaming.MultiverseStreaming(cgx_instance)

