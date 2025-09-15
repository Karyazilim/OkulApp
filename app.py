from flask import Flask, render_template

app = Flask(__name__)

# Meal data structure to pass to template
meals_data = {
    'today_menu': [
        {
            'type': 'Lunch',
            'name': 'Chicken Caesar Salad',
            'description': 'Grilled chicken breast, romaine lettuce, parmesan cheese, croutons, and Caesar dressing.',
            'image_url': 'https://lh3.googleusercontent.com/aida-public/AB6AXuA55OhofuJbRQsI6vHPW3RLCerJYgqcEjPKG9pSusFw8WvLB_r_ALSRa1caP_ENdBnzJrWiWewEu7FX-nIvR5a1uROtDZIKycDPDgz3BXMFgS44HCD64tG3AfhiE2SSjpJvOuTYeafIe1_cOAyvL8Eur3ryNXJAZsa4n-PeLk13UuGYKyszfQslUsLYqcyqrfWnBCynC5bQej-dP_g_y7WjEDEPiGBA5K-qJYINbJOW8A7HCQAkJX5j1JOru3NxoMNxm-4C6FqUT9et'
        },
        {
            'type': 'Dinner',
            'name': 'Vegetarian Pasta Primavera',
            'description': 'Pasta with a medley of fresh spring vegetables in a light cream sauce.',
            'image_url': 'https://lh3.googleusercontent.com/aida-public/AB6AXuA80qY1HAqHh7EA_bCYieRGHYtx-2BlgjJPe7S7CbFVowE1meQWVie6e0o4f8xGPq7OJJJR7rOD7Nifan7wvUXivqb0jtKSU0WH6IPYvsGkXyEZXMqxLAoBJ5T5cbwFzcXC6bUTu2vBEmh_3pbq8ZM5h4N7IPOLtChnY0Q7lzbjUl9qMykuaNb7O31a2yWVKbJCdUCqKtdRj1uHajH-o1t-5VsDQXM49ozG1gCaWaVIZus8KvU3vOe7P4B8cmBOWIxjYr4LWdeN-bW0'
        }
    ],
    'dietary_info': [
        {
            'title': 'Allergens',
            'description': 'Contains gluten, dairy, and may contain traces of nuts.',
            'icon': 'warning',
            'icon_color': 'text-[var(--primary-color)]',
            'bg_color': 'bg-blue-100'
        },
        {
            'title': 'Nutritional Value',
            'description': 'Provides a balanced mix of protein, carbohydrates, and healthy fats.',
            'icon': 'spa',
            'icon_color': 'text-green-500',
            'bg_color': 'bg-green-100'
        }
    ]
}

@app.route('/')
def index():
    """Render the Meal Plan page with meal data"""
    return render_template('index.html', **meals_data)

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors by returning to index with a message"""
    return render_template('index.html', **meals_data), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)