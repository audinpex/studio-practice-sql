from supabase import create_client, Client
import os
import dotenv

def get_client() -> Client:
    dotenv.load_dotenv()
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    return create_client(url, key)

def main():
    supabase = get_client()

    response = supabase.table("video_games_test_data").select("game_title, platform, rating, price").neq("rating", "M").limit(5).execute()
    print("Rows:")
    for row in response.data:
        print(row)

if __name__ == "__main__":
    main()