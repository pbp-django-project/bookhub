
document.getElementById('book-search-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const searchQuery = document.getElementById('search-input').value;
    const filter = document.getElementById('books-filter').value;

    try {
        // Use the Fetch API to send an AJAX request to the Django view
        const response = await fetch(`/search/?q=${searchQuery}&filter=${filter}`);

        // Parse the response as JSON
        const data = await response.json();

        // Get a reference to the HTML element where search results will be displayed
        const searchResults = document.getElementById('collection');

        // Clear previous results
        searchResults.innerHTML = '';
        let htmlString = ``
        // Loop through the books in the response and display them as list items
        data.forEach(book => {
            htmlString += `\n
            <div class="bg-white shadow-lg rounded-lg cursor-grab">
                <img src="{{ book.cover_img }}" class="rounded-t-lg w-full h-64 object-cover">
                <div class="p-4">
                    <h2 class="text-lg font-semibold">{{ book.title }}</h2>
                    <p class="text-sm">Author: {{ book.authors }}</p>
                    <p class="text-sm">Publisher: {{ book.publisher }}</p>
                    <p class="text-sm">ISBN: {{ book.isbn }}</p>
                    <p class="text-sm">Pub Year: {{ book.pub_year }}</p>
                </div>
            </div>`
        });
    } catch (error) {
        // Handle any errors that may occur during the AJAX request
        console.error('Error:', error);
    }

});

async function refreshBooks() {
    document.getElementById("collection").innerHTML = ""
    const books = await getBooks()
    let htmlString = ``
    books.forEach((book) => {
        htmlString += `\n
        <div class="bg-white shadow-lg rounded-lg cursor-grab">
            <img src="{{ book.cover_img }}" class="rounded-t-lg w-full h-64 object-cover">
            <div class="p-4">
                <h2 class="text-lg font-semibold">{{ book.title }}</h2>
                <p class="text-sm">Author: {{ book.authors }}</p>
                <p class="text-sm">Publisher: {{ book.publisher }}</p>
                <p class="text-sm">ISBN: {{ book.isbn }}</p>
                <p class="text-sm">Pub Year: {{ book.pub_year }}</p>
            </div>
        </div>`
    })

    document.getElementById("weapons_list").innerHTML = htmlString
}