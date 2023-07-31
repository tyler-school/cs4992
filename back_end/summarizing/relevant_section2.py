from textblob import TextBlob
def find_relevant_sections(corpus, search_term):
    sections = corpus.split('\n\n') # Split article into sections 
    relevant_sections = []
    
    for section in sections:
        if search_term.lower() in section.lower():
            # Split section into sentences 
            txt_obj = TextBlob(corpus)
            sentences = txt_obj.raw_sentences
            relevant_sentences = []

            for i, sentence in enumerate(sentences):
                if search_term.lower() in sentence.lower():
                    # Add the sentence 
                    start_idx = max(0, i)
                    end_idx = min(len(sentences), i)
                    relevant_sentences.extend(sentences[start_idx:end_idx + 1])

            relevant_section = '. '.join(relevant_sentences)
            relevant_sections.append(relevant_section)

    return relevant_sections

if __name__ == "__main__":
    corpus = """
Wimbledon 2023: Where to watch the tennis in London - five screenings
We’ve rounded up five of the best spots in the capital to watch Wimbledon on the big screen.

Lynn Rusk
By Lynn Rusk
Published 14th Jun 2023, 16:49 BST
Updated 15th Jun 2023, 12:25 BST

It’s time to start stocking up on Pimm’s and strawberries and cream as it’s almost Wimbledon season.

For those of you who weren’t lucky enough to secure tickets in the ballot, there are plenty of places in London to soak up the atmosphere amongst fellow tennis fans.

Advertisement


This year the world famous tennis tournament will run from Monday July 3 to Sunday July 16.

Most Popular
We’ve rounded up five of the best spots in the capital to watch Wimbledon on the big screen.

Summers Screens at Canary Wharf
Summers Screens at Canary Wharf
Watch Wimbledon 2023 at Canary Wharf


ADVERTISING

Canada Square Park and Cabot Square Free entry, usually runs 11am-7pm daily throughout the tournament

Sponsored Links
Recommended by
Cheap All-Inclusive Holidays That Will Leave You Breathless (Take A Look)
Cheap All-Inclusive Holidays That Will Leave You Breathless (Take A Look)
Affordable Holidays | Search Ads
The New £23 per Month Private Medical Insurance That's Sweeping the UK
The New £23 per Month Private Medical Insurance That's Sweeping the UK
Learn More
Health Window - Private Medical Insurance
As part of the Summer Screens series of events, Wimbledon matches are broadcast for free on a screen in Canary Wharf’s Canada Square Park and Cabot Square.

Advertisement


The same screen also hosts free open-air Movie Nights throughout the summer.



ADVERTISING

You can enjoy summer refreshments from The Grandstand Bar and a selection of summery alfresco bars, while cheering on your favourite player.

Wimbledon screening at St Katharine Docks
St Katharine Docks Marina, 50 St Katharine’s Way, E1W 1LA

Free entry

With free entry throughout the tournament, St Katharine’s Docks will be hosting Wimbledon screenings on a floating pontoon.

Comfy deck chairs are provided for free on a first come, first served basis, though picnic benches and tables will also be set up, ideal if you’re planning on bringing a picnic and making a day of it.

Wimbledon screening at Granary Square, King’s Cross
Canalside Steps, Granary Square, King’s Cross

Free entry

Advertisement


Take a seat on the steps at Granary Square (King’s Cross) during the Championships to watch the Centre Court action on the big screen, set up just across the canal.

The screen doubles up as an outdoor cinema, with cult classics and family favourites shown for free throughout the summer.

The Wimbledon finals will be screened at Greenwich Peninsula
The Wimbledon finals will be screened at Greenwich Peninsula
Wimbledon finals at Greenwich Peninsula
Canteen Food Hall & Bar, 7 Soames Walk, Greenwich Peninsula, SE10 0AX July 15 & 16 Free

Built around the O2 Arena and the glass-fronted North Greenwich Tube Station, Greenwich Peninsula is one of the capital’s most vibrant, modern living spaces.

Advertisement


There will be a giant open air screen showing the men’s and women’s finals, complete with food and drink vendors and tonnes of deck chairs for the perfect screening party experience.

Read More
Wimbledon set to lift ban on Russian and Belarusian players competing but will enforce new strict conditions
Wimbledon set to lift ban on Russian and Belarusian players competing but will enforce new strict conditions
Taste Of London Food Festival 2023: Full info, including restaurant line-up and opening times
Taste Of London Food Festival 2023: Full info, including restaurant line-up and opening times
London Pride 2023: Five celebratory events in June
London Pride 2023: Five celebratory events in June
Wimbledon screening at Covent Garden
Free

Covent Garden is setting up an outdoor screen, just a stone’s throw of the tournament’s official outfitter, Polo Ralph Lauren.

Sit back and relax with the iconic Piazza background as you watch some of the world’s greatest tennis stars take on the title of Wimbledon champion.
    """

    search_term = input("Enter your search term here: ")
    relevant_sections = find_relevant_sections(corpus, search_term)

    if relevant_sections:
        print(len(relevant_sections))
        for idx, section in enumerate(relevant_sections, start=1):
            print(f"{section}")
    else:
        print("No relevant sections found.")


        

