o
    (&�e}  �                   @   sd   d dl mZmZmZmZmZ ee�Ze�d�dd� �Z	e�d�dd� �Z
ejdd	gd
�dd� �ZdS )�    )�Flask�render_template�redirect�url_for�request�/c                   C   s   t d�S )Nz	html.html)r   � r   r   �/workspaces/python/web.py�home   �   r
   z/success/<name>c                 C   s   d|  S )Nz
welcome %sr   ��namer   r   r	   �success
   r   r   z/data�POST)�methodsc                  C   s   t jd } ttd| d��S )NZfmovier   r   )r   �formr   r   )�userr   r   r	   �data   s   
r   N)�flaskr   r   r   r   r   �__name__�app�router
   r   r   r   r   r   r	   �<module>   s   

