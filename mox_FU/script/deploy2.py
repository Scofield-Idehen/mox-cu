from src import fav_fav
def deploy_fav():
    fav_co = fav_fav.deploy() 
    return fav_co  # Return the deployed contract for further testing and usage.

def mocassin_main():
    deploy_fav()