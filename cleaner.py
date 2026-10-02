
import re

class DataCleaner:
    EMAIL_PATTERN = r"^[\w.\-]+@[\w\-]+\.\w+$"
    def __init__(self,rows):
        self.rows = rows
        self.valid_rows = []
        self.invalid_rows = []
        self.duplicates_count = 0
    @staticmethod
    def is_valid_email (email):
        """ Checks eamil formats"""
        if not email:
            return False
        return bool(re.match(DataCleaner.EMAIL_PATTERN,email.strip()))

    @staticmethod
    def is_valid_phone (phone):
        """Checks phone linghts"""
        if not phone:
            return False
        digit_only = re.sub(r"\D","",phone)
        return len(digit_only) >= 11

    def cleaner_text_fields (self,fields):
        """Trims extra sapaces."""
        
        for row in self.rows:
            for field in fields:
                if row.get(field):
                    row[field] = re.sub(r"\s+"," ",row[field].strip())
        return self

    def duplicates_remove (self):
        """Remove duplicates rows."""
        seen = set()
        unique_rows = []
        for row in self.rows:
            key = (
                (row.get("name") or "").strip().lower(),
                (row.get("email") or "").strip().lower(),
            )
            if key in seen:
                self.duplicates_count += 1
                continue
            seen.add(key)
            unique_rows.append(row)
        self.rows = unique_rows
        return self

    def validate (self):
        """Splits valid vs invalid rows."""

        for row in self.rows:
            ok_email = self.is_valid_email(row.get("email",""))
            ok_phone = self.is_valid_phone(row.get("phone",""))

            if ok_email and ok_phone:
                self.valid_rows.append(row)
            else:
                reasons = []
                if not ok_email:
                    reasons.append("invalid_email")
                if not ok_phone:
                    reasons.append("invalid_phone")
                row["error_reasons"] = ",".join(reasons)
                self.invalid_rows.append(row)
        return self
    def summary (self):
        """Returns result counts."""
        total_processed = len(self.valid_rows) + len(self.invalid_rows) + (self.duplicates_count)

        return {
            "total_processed": total_processed,
            "valid_rows": self.valid_rows,
            "invalid_rows": self.invalid_rows,
            "duplicates_count": self.duplicates_count
        }
    