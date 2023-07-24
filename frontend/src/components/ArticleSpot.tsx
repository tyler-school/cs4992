// ArticleSpot.tsx

import React from 'react';

interface ArticleSpotProps {
  title: string;
  link: string;
  date: string;
}

const ArticleSpot: React.FC<ArticleSpotProps> = ({ title, link, date }) => {
  return (
    <div className="article-spot">
      <h3>{title}</h3>
      <p>Date: {date}</p>
      <a href={link}>Read More</a>
    </div>
  );
};

export default ArticleSpot;
