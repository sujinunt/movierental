package movierental;
/**
 * A movie available for rent.
 */
public class Movie {
	/** The classes of movies. */
	public static final int REGULAR = 0;
	public static final int NEW_RELEASE = 1;
	public static final int CHILDRENS = 2;
	
	/** movie price code based on classification */
	private int priceCode;
	/** the title, of course */
	private String title;
	
	/** Initialize a new movie. */
	public Movie(String title, int priceCode) {
		this.title = title;
		this.priceCode = priceCode;
	}

	/**
	 * @return the priceCode
	 */
	public int getPriceCode() {
		return priceCode;
	}

	/**
	 * @param priceCode the priceCode to set
	 */
	public void setPriceCode(int priceCode) {
		this.priceCode = priceCode;
	}
	
	/** Return the movie title */
	public String getTitle() {
		return this.title;
	}
	
	public String toString() {
		return this.title;
	}
}
