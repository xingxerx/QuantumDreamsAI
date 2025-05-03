# Assuming module is renamed to cgx_api.py and class to CgxApi
import cgx_api
import multiverse_streaming
import parallel_universe_api

# Initialize CGX API
cgx_instance = cgx_api.CgxApi() # Using PascalCase for class, snake_case for variable

# Set up multiverse streaming
streaming = multiverse_streaming.MultiverseStreaming(cgx_instance)

# Set up parallel universe API
parallel_api = parallel_universe_api.ParallelUniverseAPI(cgx_instance)

# Channel configuration
