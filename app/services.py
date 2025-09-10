from app.repository import load_users
from math import ceil

def filter_users(users, q=None, role=None, is_active=None):
    filtered = users
    if q:
        q_lower = q.lower()
        filtered = [u for u in filtered if q_lower in u.get('name', '').lower() or q_lower in u.get('email', '').lower()]
    if role:
        filtered = [u for u in filtered if u.get('role', '').lower() == role.lower()]
    if is_active is not None:
        filtered = [u for u in filtered if u.get('is_active') == is_active]
    return filtered

def paginate_users(users, page, page_size):
    total_items = len(users)
    total_pages = ceil(total_items / page_size) if page_size else 1
    if page < 1 or page > total_pages:
        return [], total_items, total_pages
    start = (page - 1) * page_size
    end = start + page_size
    return users[start:end], total_items, total_pages

def get_users(page=1, page_size=10, q=None, role=None, is_active=None):
    users = load_users()
    filtered = filter_users(users, q, role, is_active)
    paginated, total_items, total_pages = paginate_users(filtered, page, page_size)
    return {
        "data": paginated,
        "pagination": {
            "current_page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages
        }
    }

def get_user_by_id(user_id):
    users = load_users()
    for user in users:
        if user.get('id') == user_id:
            return user
    return None