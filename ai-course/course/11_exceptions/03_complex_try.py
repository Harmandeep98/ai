def serve_chai(flavour):
    try:
        if flavour == "unknown":
            raise ValueError(f"We do not know which flavour is {flavour}")
        print(f"Preparing {flavour} chai...")
    except ValueError as e:
        print(f"Error {e}")
    else:
        print(f"Chai with flavour {flavour} is served")
    finally:
        print("Next customer please");


# serve_chai("Masala")

serve_chai("unknown")