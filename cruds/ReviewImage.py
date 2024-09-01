from config.database import database
from models.ReviewImage import ReviewImage

async def get_all_review_images():
    query = "SELECT * FROM review_image"
    result = await database.fetch_all(query=query)
    return result

async def   get_review_image(review_image_id: int):
    query = "SELECT * FROM review_image WHERE review_id = :review_id"
    return await database.fetch_all(query=query, values={"review_id": review_image_id})

async def create_review_image(review_image: ReviewImage):
    query = """
    INSERT INTO review_image (review_id, filename, created_by)
    VALUES (:review_id, :filename, :created_by)
    """
    values = {
        "review_id": review_image.review_id,
        "filename": review_image.filename,
        "created_by": review_image.created_by,
    }
    await database.execute(query=query, values=values)

async def update_review_image(review_image_id: int, review_image: ReviewImage):
    query = """
    UPDATE review_image
    SET review_id = :review_id, filename = :filename, created_by = :created_by,
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**review_image.dict(), "id": review_image_id}
    await database.execute(query=query, values=values)

async def delete_review_image(review_image_id: int):
    query = "DELETE FROM review_image WHERE id = :id"
    await database.execute(query=query, values={"id": review_image_id})
