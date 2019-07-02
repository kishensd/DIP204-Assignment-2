function activeTab(){
    if (page = document.getElementById('this_page').textContent){
        document.getElementById(page).classList.add('text-primary')
    }
}
activeTab()