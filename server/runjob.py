from services.similarity_service import *
from services.mongodb import *

events_sim = events_sim_with_loc(id, location)
update_events_table(id, events_sim)