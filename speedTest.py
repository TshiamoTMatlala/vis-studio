import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    
    # Find the best server for accurate results
    st.get_best_server()
    
    # Measure download, upload, and ping latency
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    ping_latency = st.results.ping  # in ms
    
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping Latency: {ping_latency} ms")

if __name__ == "__main__":
    check_internet_speed()
