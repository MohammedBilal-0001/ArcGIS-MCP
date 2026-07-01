class SearchQueryBuilder:
    @staticmethod
    def build(
        query: str,
        owner: str |None = None,
        item_type: str |None = None,
        num: int = 10,
        orgid: str |None = None
    ) -> str:

        parts = []

        if query:
            parts.append(query)
        
        if owner:
            parts.append(f"owner:{owner}")
        
        if item_type:
            parts.append(f'type:"{item_type}"')
        
        # if num:
        #     parts.append(f"num:{num}")
        
        if orgid:
            parts.append(f"orgid:{orgid}")
        
        return " ".join(parts)

