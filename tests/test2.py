from pytube import StreamQuery, YouTube, Playlist
import threading
import time

'''
streams = list()
urls    = [
        'https://youtu.be/zLTAXQW96Do?si=653hhVCoanHPoOTC',
        'https://youtu.be/ZZ3BWmXGAGY?si=wO5R3ywZqbB9wsFo',
        'https://youtu.be/AZt0c1L60fw?si=_2U8B9L8570RR6zQ',
        'https://youtu.be/M04JlWTRQEA?si=7fUvX32CG9qA9BwQ',
        'https://youtu.be/Fu-CcQWiiKc?si=ugLLRI20Bc9QKRkR'
        ]

def getStream(url) -> StreamQuery:
    yt = YouTube(url)
    return yt.streams

a = time.time()
for i in urls:
    streams.append(threading.Thread(target=getStream, args=(i,)).start()) 
b = time.time()

for i in streams:
    for j in i:
        print(j)

print('\n', b-a)

from pytube import YouTube
import concurrent.futures

# Function to get streams for a single video
def get_streams(video_url):
    try:
        yt = YouTube(video_url)
        streams = yt.streams
        print(f"Streams for {video_url} retrieved successfully.")
    except Exception as e:
        print(f"Error retrieving streams for {video_url}: {e}")

# List of video URLs
# Use ThreadPoolExecutor to manage threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map the function to the video URLs
    executor.map(get_streams, video_urls)

print("All streams retrieved.")


from pytube import YouTube
import asyncio
import concurrent.futures


# Function to get streams for a single video
def get_streams(video_url):
    try:
        yt = YouTube(video_url)
        streams = yt.streams
        print(f"Streams for {video_url} retrieved successfully.")
    except Exception as e:
        print(f"Error retrieving streams for {video_url}: {e}")

# List of video URLs


async def main():
    # Use ThreadPoolExecutor to manage threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Run get_streams function concurrently
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(executor, get_streams, url)
            for url in video_urls
        ]
        await asyncio.gather(*tasks)

# Run the async main function
asyncio.run(main())

print("All streams retrieved.")

from pytube import YouTube
import asyncio
import concurrent.futures
import time

# Function to get streams for a single video
def get_streams(video_url):
    try:
        yt = YouTube(video_url)
        streams = yt.streams
        print(f"Streams for {video_url} retrieved successfully.")
    except Exception as e:
        print(f"Error retrieving streams for {video_url}: {e}")

# List of video URLs (adjust as needed)

video_urls = [
        'https://youtu.be/zLTAXQW96Do?si=653hhVCoanHPoOTC',
        'https://youtu.be/ZZ3BWmXGAGY?si=wO5R3ywZqbB9wsFo',
        'https://youtu.be/AZt0c1L60fw?si=_2U8B9L8570RR6zQ',
        'https://youtu.be/M04JlWTRQEA?si=7fUvX32CG9qA9BwQ',
]
async def main(concurrency_limit=10):
    # Use ThreadPoolExecutor to manage threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency_limit) as executor:
        # Run get_streams function concurrently with a limit on concurrency
        loop = asyncio.get_event_loop()
        tasks = []
        for url in video_urls:
            if len(tasks) >= concurrency_limit:
                await asyncio.gather(*tasks)
                tasks = []
            task = loop.run_in_executor(executor, get_streams, url)
            tasks.append(task)
        if tasks:
            await asyncio.gather(*tasks)

# Set your desired concurrency limit here
CONCURRENCY_LIMIT = 10

# Measure start time
start_time = time.time()

# Run the async main function
asyncio.run(main(concurrency_limit=CONCURRENCY_LIMIT))

# Measure end time
end_time = time.time()

print(f"All streams retrieved in {end_time - start_time:.2f} seconds.")
'''
from pytube import YouTube
import concurrent.futures
import time

# Function to get streams for a single video
def get_streams(video_url):
    try:
        yt = YouTube(video_url)
        streams = yt.streams
        print(f"Streams for {video_url} retrieved successfully.")
    except Exception as e:
        print(f"Error retrieving streams for {video_url}: {e}")

# List of video URLs

video_urls = [
        'https://youtu.be/zLTAXQW96Do?si=653hhVCoanHPoOTC',
        'https://youtu.be/ZZ3BWmXGAGY?si=wO5R3ywZqbB9wsFo',
        'https://youtu.be/AZt0c1L60fw?si=_2U8B9L8570RR6zQ',
        'https://youtu.be/M04JlWTRQEA?si=7fUvX32CG9qA9BwQ',
]

def fetch_all_streams(video_urls, concurrency_limit=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency_limit) as executor:
        # Map the get_streams function to the video URLs
        executor.map(get_streams, video_urls)

# Measure start time
start_time = time.time()

# Set your desired concurrency limit here
CONCURRENCY_LIMIT = 10

# Fetch streams for all video URLs
fetch_all_streams(video_urls, concurrency_limit=CONCURRENCY_LIMIT)

# Measure end time
end_time = time.time()

print(f"All streams retrieved in {end_time - start_time:.2f} seconds.")


a = time.time()

for i in video_urls:
    yt=YouTube(i)
    yt.streams
b = time.time()
print(b-a)
